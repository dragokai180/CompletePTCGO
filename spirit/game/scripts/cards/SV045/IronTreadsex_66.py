from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e0a5f35-d353-5d42-b9ca-d17f3289736d',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name',
    display_name='Iron Treads ex',
    searchable_by=['Iron Treads ex', 'Basic', 'ex', 'Future', 'IronTreadsex'],
    subtypes=['Basic', 'ex', 'Future'],
    collector_number=66,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=990,
    abilities=[
        Attack(
            title='Iron-Clad Roll',
            game_text="After doing damage, you may discard all Future Booster Energy Capsules from this Pokémon. If you do, during your opponent's next turn, this Pokémon takes 150 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
