from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0cca3079-2043-5d2b-8c4f-d84ee1201ed1',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name',
    display_name='Prinplup',
    searchable_by=['Prinplup', 'Stage 1', 'Prinplup'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name',
    family_id=393,
    abilities=[
        Attack(
            title='Ice Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
