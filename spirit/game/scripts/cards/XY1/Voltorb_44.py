from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e26087cc-fcf2-5030-b402-1a68f18d72dd',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    display_name='Voltorb',
    searchable_by=['Voltorb', 'Basic', 'Voltorb'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=100,
    abilities=[
        Ability(
            title='Destiny Burst',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, put 5 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, put 5 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
