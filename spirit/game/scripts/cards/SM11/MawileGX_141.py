from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7403c668-d3bb-5660-be02-0c4fc87517b3',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MawileGX.Name',
    display_name='Mawile-GX',
    searchable_by=['Mawile-GX', 'Basic', 'GX', 'MawileGX'],
    subtypes=['Basic', 'GX'],
    collector_number=141,
    set_code='SM11',
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
    family_id=303,
    abilities=[
        Ability(
            title='Captivating Wink',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may have your opponent reveal their hand and put any number of Basic Pokémon you find there onto their Bench.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Wily Bite',
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Big Eater-GX',
            game_text="Your opponent reveals their hand. Discard all Supporter cards you find there. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
