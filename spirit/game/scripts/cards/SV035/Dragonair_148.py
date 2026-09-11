from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b53dc41-fe61-5e5f-a2f7-da943b2b0558',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    display_name='Dragonair',
    searchable_by=['Dragonair', 'Stage 1', 'Dragonair'],
    subtypes=['Stage 1'],
    collector_number=148,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Aqua Slash',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
