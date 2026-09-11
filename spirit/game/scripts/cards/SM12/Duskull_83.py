from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='09dc5622-e044-5921-b43b-047591a49587',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name',
    display_name='Duskull',
    searchable_by=['Duskull', 'Basic', 'Duskull'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=355,
    abilities=[
        Ability(
            title='Spiritborne Evolution',
            game_text='Once during your turn (before your attack), you may discard 3 cards from your hand. If you do, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Ominous Eyes',
            game_text="Put 2 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
