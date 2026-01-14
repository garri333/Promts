#!/usr/bin/env python3
"""
SCRIPT DE BÚSQUEDA MULTI-DIMENSIONAL DE PROMPTS
Utilitza les metadades YAML per fer búsquedas avançades
"""

import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class PromptMetadata:
    """Estructura de metadades d'un prompt"""
    prompt_id: str
    name: str
    domain: str
    use_case: str
    framework: List[str]
    agent_type: str
    techniques: List[str]
    role: str
    task: str
    format: str
    tools: List[str]
    metrics: Dict[str, Any]
    version: str
    created_at: str
    updated_at: str
    author: str
    file_path: str = ""


class PromptDatabase:
    """Base de dades de prompts amb búsqueda multi-dimensional"""
    
    def __init__(self, library_path: str = "../categories"):
        self.library_path = Path(library_path)
        self.prompts: List[PromptMetadata] = []
        self.load_all_prompts()
    
    def load_all_prompts(self):
        """Carrega tots els prompts de totes les categories"""
        for category_file in self.library_path.glob("*.md"):
            self._parse_category_file(category_file)
    
    def _parse_category_file(self, file_path: Path):
        """Parsea un fitxer de categoria i extreu prompts"""
        content = file_path.read_text(encoding='utf-8')
        
        # Buscar blocs YAML dins del fitxer
        in_yaml = False
        yaml_content = []
        
        for line in content.split('\n'):
            if line.strip() == '```yaml':
                in_yaml = True
                yaml_content = []
            elif line.strip() == '```' and in_yaml:
                in_yaml = False
                # Intentar parsear el bloc YAML
                try:
                    metadata_dict = yaml.safe_load('\n'.join(yaml_content))
                    if metadata_dict and 'prompt_id' in metadata_dict:
                        # Convertir a dataclass
                        prompt = PromptMetadata(
                            prompt_id=metadata_dict.get('prompt_id', ''),
                            name=metadata_dict.get('name', ''),
                            domain=metadata_dict.get('domain', ''),
                            use_case=metadata_dict.get('use_case', ''),
                            framework=metadata_dict.get('framework', []),
                            agent_type=metadata_dict.get('agent_type', ''),
                            techniques=metadata_dict.get('techniques', []),
                            role=metadata_dict.get('role', ''),
                            task=metadata_dict.get('task', ''),
                            format=metadata_dict.get('format', ''),
                            tools=metadata_dict.get('tools', []),
                            metrics=metadata_dict.get('metrics', {}),
                            version=metadata_dict.get('version', ''),
                            created_at=metadata_dict.get('created_at', ''),
                            updated_at=metadata_dict.get('updated_at', ''),
                            author=metadata_dict.get('author', ''),
                            file_path=str(file_path)
                        )
                        self.prompts.append(prompt)
                except Exception as e:
                    print(f"Error parsing YAML in {file_path}: {e}")
            elif in_yaml:
                yaml_content.append(line)
    
    # BÚSQUEDAS PER PROBLEMA DE NEGOCI
    
    def search_by_domain(self, domain: str) -> List[PromptMetadata]:
        """Busca prompts per domini de negoci"""
        return [p for p in self.prompts if domain.lower() in p.domain.lower()]
    
    def search_by_use_case(self, use_case: str) -> List[PromptMetadata]:
        """Busca prompts per cas d'ús específic"""
        return [p for p in self.prompts if use_case.lower() in p.use_case.lower()]
    
    # REUTILITZACIÓ AMB DIFERENTS FRAMEWORKS
    
    def search_by_framework(self, framework: str) -> List[PromptMetadata]:
        """Busca prompts compatibles amb un framework"""
        return [p for p in self.prompts if framework in p.framework]
    
    def search_multi_framework(self, frameworks: List[str]) -> List[PromptMetadata]:
        """Busca prompts compatibles amb múltiples frameworks"""
        return [p for p in self.prompts if any(f in p.framework for f in frameworks)]
    
    # BÚSQUEDA PER TIPUS D'AGENT
    
    def search_by_agent_type(self, agent_type: str) -> List[PromptMetadata]:
        """Busca prompts per tipus d'agent"""
        return [p for p in self.prompts if p.agent_type == agent_type]
    
    # BÚSQUEDA PER TÈCNIQUES
    
    def search_by_technique(self, technique: str) -> List[PromptMetadata]:
        """Busca prompts que utilitzen una tècnica específica"""
        return [p for p in self.prompts if technique in p.techniques]
    
    # MESURA DE RENDIMENT
    
    def search_by_rating(self, min_rating: float = 4.5) -> List[PromptMetadata]:
        """Busca prompts amb rating mínim"""
        return [p for p in self.prompts if p.metrics.get('rating', 0) >= min_rating]
    
    def search_production_ready(self) -> List[PromptMetadata]:
        """Busca només prompts production-ready"""
        return [p for p in self.prompts if p.metrics.get('production_ready', False)]
    
    def search_by_cost(self, max_cost: float = 0.05) -> List[PromptMetadata]:
        """Busca prompts econòmics"""
        return [p for p in self.prompts if p.metrics.get('avg_cost', 999) <= max_cost]
    
    def search_by_latency(self, max_latency_ms: int = 1500) -> List[PromptMetadata]:
        """Busca prompts ràpids"""
        return [p for p in self.prompts if p.metrics.get('latency_ms', 999999) <= max_latency_ms]
    
    def search_low_hallucination(self, max_rate: float = 0.03) -> List[PromptMetadata]:
        """Busca prompts amb baixa taxa d'al·lucinacions"""
        return [p for p in self.prompts if p.metrics.get('hallucination_rate', 1.0) <= max_rate]
    
    # BÚSQUEDA COMBINADA
    
    def advanced_search(
        self,
        domain: Optional[str] = None,
        use_case: Optional[str] = None,
        framework: Optional[str] = None,
        agent_type: Optional[str] = None,
        technique: Optional[str] = None,
        min_rating: Optional[float] = None,
        production_ready: Optional[bool] = None,
        max_cost: Optional[float] = None,
        max_latency: Optional[int] = None
    ) -> List[PromptMetadata]:
        """Búsqueda avançada amb múltiples criteris"""
        results = self.prompts.copy()
        
        if domain:
            results = [p for p in results if domain.lower() in p.domain.lower()]
        
        if use_case:
            results = [p for p in results if use_case.lower() in p.use_case.lower()]
        
        if framework:
            results = [p for p in results if framework in p.framework]
        
        if agent_type:
            results = [p for p in results if p.agent_type == agent_type]
        
        if technique:
            results = [p for p in results if technique in p.techniques]
        
        if min_rating is not None:
            results = [p for p in results if p.metrics.get('rating', 0) >= min_rating]
        
        if production_ready is not None:
            results = [p for p in results if p.metrics.get('production_ready', False) == production_ready]
        
        if max_cost is not None:
            results = [p for p in results if p.metrics.get('avg_cost', 999) <= max_cost]
        
        if max_latency is not None:
            results = [p for p in results if p.metrics.get('latency_ms', 999999) <= max_latency]
        
        return results
    
    # ESTADÍSTIQUES
    
    def get_statistics(self) -> Dict[str, Any]:
        """Genera estadístiques de la biblioteca"""
        return {
            'total_prompts': len(self.prompts),
            'by_domain': self._count_by_field('domain'),
            'by_framework': self._count_by_framework(),
            'by_agent_type': self._count_by_field('agent_type'),
            'by_technique': self._count_by_techniques(),
            'avg_rating': self._calculate_avg_rating(),
            'production_ready_count': len(self.search_production_ready()),
            'avg_cost': self._calculate_avg_cost(),
            'avg_latency': self._calculate_avg_latency()
        }
    
    def _count_by_field(self, field: str) -> Dict[str, int]:
        """Compta prompts per un camp específic"""
        counts = {}
        for prompt in self.prompts:
            value = getattr(prompt, field, 'Unknown')
            counts[value] = counts.get(value, 0) + 1
        return counts
    
    def _count_by_framework(self) -> Dict[str, int]:
        """Compta prompts per framework"""
        counts = {}
        for prompt in self.prompts:
            for fw in prompt.framework:
                counts[fw] = counts.get(fw, 0) + 1
        return counts
    
    def _count_by_techniques(self) -> Dict[str, int]:
        """Compta prompts per tècnica"""
        counts = {}
        for prompt in self.prompts:
            for tech in prompt.techniques:
                counts[tech] = counts.get(tech, 0) + 1
        return counts
    
    def _calculate_avg_rating(self) -> float:
        """Calcula rating mitjà"""
        ratings = [p.metrics.get('rating', 0) for p in self.prompts]
        return sum(ratings) / len(ratings) if ratings else 0
    
    def _calculate_avg_cost(self) -> float:
        """Calcula cost mitjà"""
        costs = [p.metrics.get('avg_cost', 0) for p in self.prompts]
        return sum(costs) / len(costs) if costs else 0
    
    def _calculate_avg_latency(self) -> float:
        """Calcula latència mitjana"""
        latencies = [p.metrics.get('latency_ms', 0) for p in self.prompts]
        return sum(latencies) / len(latencies) if latencies else 0


# EXEMPLES D'ÚS

def main():
    """Exemples de búsquedas"""
    db = PromptDatabase()
    
    print("=" * 80)
    print("EXEMPLES DE BÚSQUEDA MULTI-DIMENSIONAL")
    print("=" * 80)
    
    # 1. BÚSQUEDA PER PROBLEMA DE NEGOCI
    print("\n1. Búsqueda per domini 'Planning':")
    results = db.search_by_domain("Planning")
    for p in results[:3]:
        print(f"  - {p.name} (rating: {p.metrics.get('rating', 'N/A')})")
    
    # 2. REUTILITZACIÓ AMB DIFERENTS FRAMEWORKS
    print("\n2. Prompts compatibles amb 'LangChain':")
    results = db.search_by_framework("LangChain")
    for p in results[:3]:
        print(f"  - {p.name} (frameworks: {', '.join(p.framework)})")
    
    # 3. FILTRATGE PER QUALITAT
    print("\n3. Prompts production-ready amb rating >= 4.7:")
    results = db.advanced_search(min_rating=4.7, production_ready=True)
    for p in results[:3]:
        print(f"  - {p.name} (rating: {p.metrics.get('rating')})")
    
    # 4. OPTIMITZACIÓ DE COSTOS
    print("\n4. Prompts barats (<0.05$) i ràpids (<1500ms):")
    results = db.advanced_search(max_cost=0.05, max_latency=1500)
    for p in results[:3]:
        cost = p.metrics.get('avg_cost', 'N/A')
        latency = p.metrics.get('latency_ms', 'N/A')
        print(f"  - {p.name} (cost: ${cost}, latency: {latency}ms)")
    
    # 5. BÚSQUEDA PER TÈCNICA
    print("\n5. Prompts que utilitzen 'Chain-of-Thought':")
    results = db.search_by_technique("Chain-of-Thought")
    for p in results[:3]:
        print(f"  - {p.name} (techniques: {', '.join(p.techniques)})")
    
    # 6. ESTADÍSTIQUES GENERALS
    print("\n6. Estadístiques de la biblioteca:")
    stats = db.get_statistics()
    print(f"  - Total prompts: {stats['total_prompts']}")
    print(f"  - Rating mitjà: {stats['avg_rating']:.2f}")
    print(f"  - Production ready: {stats['production_ready_count']}")
    print(f"  - Cost mitjà: ${stats['avg_cost']:.3f}")
    print(f"  - Latència mitjana: {stats['avg_latency']:.0f}ms")
    
    print(f"\n  - Prompts per domini:")
    for domain, count in sorted(stats['by_domain'].items())[:5]:
        print(f"    * {domain}: {count}")
    
    print(f"\n  - Prompts per framework:")
    for fw, count in sorted(stats['by_framework'].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"    * {fw}: {count}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
