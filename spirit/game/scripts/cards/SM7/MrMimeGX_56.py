from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='97cc3085-08be-580c-8827-cc1694bf9a97',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name',
    display_name='Mr. Mime-GX',
    searchable_by=['Mr. Mime-GX', 'Basic', 'GX', 'MrMimeGX'],
    subtypes=['Basic', 'GX'],
    collector_number=56,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title='Magic Evens',
            game_text="Prevent all damage done to this Pokémon by your opponent's attacks if that damage is exactly 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, or 260.",
            passive=standard_passive("Prevent all damage done to this Pokémon by your opponent's attacks if that damage is exactly 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, or 260."),
        ),
        Attack(
            title='Breakdown',
            game_text="For each card in your opponent's hand, put 1 damage counter on their Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Life Trick-GX',
            game_text="Heal all damage from this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
