from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3318452a-657a-5640-9837-3b8642f7539a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name',
    display_name='Audino',
    searchable_by=['Audino', 'Basic', 'Audino'],
    subtypes=['Basic'],
    collector_number=177,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=531,
    abilities=[
        Ability(
            title='Hearing',
            game_text='Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Drain Slap',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
