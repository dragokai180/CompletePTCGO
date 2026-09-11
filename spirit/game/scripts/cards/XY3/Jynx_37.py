from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f22c959e-8838-5686-91b2-d04bebe8b037',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name',
    display_name='Jynx',
    searchable_by=['Jynx', 'Basic', 'Jynx'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=124,
    abilities=[
        Ability(
            title='Victory Kiss',
            game_text='Once during your turn (before your attack), if this Pokémon is on your Bench, you may heal 10 damage from your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hug',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
