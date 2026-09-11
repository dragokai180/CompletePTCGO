from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15820eef-0e7d-5007-ba62-3a5926056e82',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LatiosGX.Name',
    display_name='Latios-GX',
    searchable_by=['Latios-GX', 'Basic', 'GX', 'LatiosGX'],
    subtypes=['Basic', 'GX'],
    collector_number=78,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Ability(
            title='Power Bind',
            game_text="If you have 4 or fewer Pokémon in play, this Pokémon can't attack.",
            passive=standard_passive("If you have 4 or fewer Pokémon in play, this Pokémon can't attack."),
        ),
        Attack(
            title='Tag Purge',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from TAG TEAM Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Clear Vision-GX',
            game_text="For the rest of this game, your opponent can't use any GX attacks. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
