from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0284d46a-c68c-52f2-af98-a629f6212108',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GuzzlordGX.Name',
    display_name='Guzzlord-GX',
    searchable_by=['Guzzlord-GX', 'Basic', 'GX', 'Ultra Beast', 'GuzzlordGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=63,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=799,
    abilities=[
        Attack(
            title='Eat Sloppily',
            game_text='Discard the top 5 cards of your deck. If any of those cards are Energy cards, attach them to this Pokémon.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tyrannical Hole',
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
        ),
        Attack(
            title='Glutton-GX',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 2 more Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 5},
            damage=100,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
