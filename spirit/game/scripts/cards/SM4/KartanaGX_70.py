from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4c98528-3aa2-5568-81ea-dd2ab97c2504',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KartanaGX.Name',
    display_name='Kartana-GX',
    searchable_by=['Kartana-GX', 'Basic', 'GX', 'Ultra Beast', 'KartanaGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=70,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=798,
    abilities=[
        Ability(
            title='Slice Off',
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Special Energy from 1 of your opponent's Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Gale Blade',
            game_text='You may shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Blade-GX',
            game_text="Take a Prize card. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
