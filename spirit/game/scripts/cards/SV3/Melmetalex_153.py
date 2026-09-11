from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d29919f-9611-57a3-b0a6-cca44cea84c7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name',
    display_name='Melmetal ex',
    searchable_by=['Melmetal ex', 'Stage 1', 'ex', 'Melmetalex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=153,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name',
    family_id=808,
    abilities=[
        Attack(
            title='Metal-bolize',
            game_text='Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Full Metal Knuckle',
            game_text='This attack does 30 more damage for each Metal Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
