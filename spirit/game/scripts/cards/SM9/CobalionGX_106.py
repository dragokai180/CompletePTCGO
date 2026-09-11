from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='811dc98b-0ee3-5d4e-89c2-cea24efd492a',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CobalionGX.Name',
    display_name='Cobalion-GX',
    searchable_by=['Cobalion-GX', 'Basic', 'GX', 'CobalionGX'],
    subtypes=['Basic', 'GX'],
    collector_number=106,
    set_code='SM9',
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
    family_id=638,
    abilities=[
        Ability(
            title='Metal Symbol',
            game_text="Each of your Pokémon that has any Metal Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pokémon.",
            passive=standard_passive("Each of your Pokémon that has any Metal Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pokémon."),
        ),
        Attack(
            title='Dueling Saber',
            game_text='If there is any Stadium card in play, this attack does 60 more damage.',
            cost={PokemonTypes.METAL: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Rule-GX',
            game_text="During your opponent's next turn, their Pokémon can't attack. (This includes Pokémon that come into play on that turn.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)
