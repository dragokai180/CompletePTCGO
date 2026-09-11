from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df6622f5-283b-5337-ba43-18b5438d7d96',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=158,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title='Lazy Eating',
            game_text='Between turns, heal 10 damage from this Pokémon.',
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Big Counter',
            game_text="If your opponent's Active Pokémon is a TAG TEAM, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
