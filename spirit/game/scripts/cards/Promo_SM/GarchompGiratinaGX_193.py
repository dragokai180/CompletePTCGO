from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f656f8b-9821-5a61-82d7-d331cf032f8c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GarchompGiratinaGX.Name',
    display_name='Garchomp & Giratina-GX',
    searchable_by=['Garchomp & Giratina-GX', 'Basic', 'TAG TEAM', 'GX', 'GarchompGiratinaGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=193,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=445,
    abilities=[
        Attack(
            title='Linear Attack',
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Calamitous Slash',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='GG End-GX',
            game_text="Discard 1 of your opponent's Pokémon and all cards attached to it. If this Pokémon has at least 3 extra Fighting Energy attached to it (in addition to this attack's cost), discard 2 of your opponent's Pokémon instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
