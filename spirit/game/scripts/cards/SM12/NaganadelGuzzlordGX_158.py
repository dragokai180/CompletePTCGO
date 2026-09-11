from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e38f6251-cb11-5fb6-abf4-d1fabfeed573',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGuzzlordGX.Name',
    display_name='Naganadel & Guzzlord-GX',
    searchable_by=['Naganadel & Guzzlord-GX', 'Basic', 'TAG TEAM', 'GX', 'Ultra Beast', 'NaganadelGuzzlordGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX', 'Ultra Beast'],
    collector_number=158,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=799,
    abilities=[
        Ability(
            title='Violent Appetite',
            game_text='Once during your turn (before your attack), you may discard a Pokémon from your hand. If you do, heal 60 damage from this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Jet Pierce',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
        Attack(
            title='Chaotic Order-GX',
            game_text="Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.) If this Pokémon has at least 1 extra Psychic Energy and 1 extra Darkness Energy attached to it (in addition to this attack's cost), take 2 Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
