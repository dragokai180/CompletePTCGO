from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b59be4a-942e-5ada-b337-23941a77fce0',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name',
    display_name='Vivillon',
    searchable_by=['Vivillon', 'Stage 2', 'Vivillon'],
    subtypes=['Stage 2'],
    collector_number=17,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    family_id=664,
    abilities=[
        Attack(
            title='Conversion Powder',
            game_text="Choose either Asleep or Poisoned. Your opponent's Active Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Colorful Wind',
            game_text='This attack does 30 more damage for each different type of basic Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
