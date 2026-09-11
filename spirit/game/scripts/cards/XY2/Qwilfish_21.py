from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d373731-726e-51cd-828b-15427d8dd7b8',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name',
    display_name='Qwilfish',
    searchable_by=['Qwilfish', 'Basic', 'Qwilfish'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=211,
    abilities=[
        Ability(
            title='Counterattack Quills',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
