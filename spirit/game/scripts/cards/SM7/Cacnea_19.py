from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3455150-da91-5370-b852-a5c5b3c75471',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name',
    display_name='Cacnea',
    searchable_by=['Cacnea', 'Basic', 'Cacnea'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=331,
    abilities=[
        Ability(
            title='Poison Payback',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned."),
        ),
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
