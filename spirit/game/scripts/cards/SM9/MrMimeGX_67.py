from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='95906460-8d77-58a0-9319-1d042c35e2fc',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name',
    display_name='Mr. Mime-GX',
    searchable_by=['Mr. Mime-GX', 'Basic', 'GX', 'MrMimeGX'],
    subtypes=['Basic', 'GX'],
    collector_number=67,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title='Magic Odds',
            game_text="Prevent all damage done to this Pokémon by your opponent's attacks if that damage is exactly 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, or 250.",
            passive=standard_passive("Prevent all damage done to this Pokémon by your opponent's attacks if that damage is exactly 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, or 250."),
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
