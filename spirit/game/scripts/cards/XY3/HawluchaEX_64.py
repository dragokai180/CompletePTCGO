from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='118c19a7-bb73-5598-8f15-b732a9510c1d',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HawluchaEX.Name',
    display_name='Hawlucha-EX',
    searchable_by=['Hawlucha-EX', 'Basic', 'EX', 'HawluchaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=64,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Ability(
            title='Counterattack',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Moonsault Stomp',
            game_text='If there is any Stadium card in play, this attack does 40 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
