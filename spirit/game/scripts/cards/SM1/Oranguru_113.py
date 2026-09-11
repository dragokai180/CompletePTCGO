from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d14b5bea-ef07-52f6-9cd3-0048da3a0f2b',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name',
    display_name='Oranguru',
    searchable_by=['Oranguru', 'Basic', 'Oranguru'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=765,
    abilities=[
        Ability(
            title='Instruct',
            game_text='Once during your turn (before your attack), you may draw cards until you have 3 cards in your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
