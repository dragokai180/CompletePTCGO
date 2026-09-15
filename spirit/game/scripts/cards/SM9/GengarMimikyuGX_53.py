from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e72e4015-48f0-530a-a88f-32226fb4a339',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GengarMimikyuGX.Name',
    display_name='Gengar & Mimikyu-GX',
    searchable_by=['Gengar & Mimikyu-GX', 'Basic', 'TAG TEAM', 'GX', 'GengarMimikyuGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=53,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=94,
    abilities=[
        Attack(
            title='Poltergeist',
            game_text='Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Horror House-GX',
            game_text="Your opponent can't play any cards from their hand during their next turn. If this Pokémon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), each player draws cards until they have 7 cards in their hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
