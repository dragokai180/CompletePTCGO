from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0ad86bc-0d75-592a-92f0-792c6f61302e',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name',
    display_name='Crabominable',
    searchable_by=['Crabominable', 'Stage 1', 'Crabominable'],
    subtypes=['Stage 1'],
    collector_number=115,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    family_id=739,
    abilities=[
        Attack(
            title='Confront',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Knuckle Impact',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
