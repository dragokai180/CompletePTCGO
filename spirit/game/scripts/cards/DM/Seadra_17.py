from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7f32ebb-7322-553b-882e-f01e8dca9dcf',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    display_name='Seadra',
    searchable_by=['Seadra', 'Stage 1', 'Seadra'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
