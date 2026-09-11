from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f4d84125-c65c-5620-a121-9b2f40662e38',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RowletAlolanExeggutorGX.Name',
    display_name='Rowlet & Alolan Exeggutor-GX',
    searchable_by=['Rowlet & Alolan Exeggutor-GX', 'Basic', 'TAG TEAM', 'GX', 'RowletAlolanExeggutorGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=1,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=103,
    abilities=[
        Attack(
            title='Super Growth',
            game_text='Search your deck for a card that evolves from 1 of your Grass Pokémon and put it onto that Pokémon to evolve it. If that Pokémon is now a Stage 1 Pokémon, search your deck for a Stage 2 Pokémon that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Calming Hurricane',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Tropical Hour-GX',
            game_text="If this Pokémon has at least 3 extra Energy attached to it (in addition to this attack's cost), your opponent shuffles all Energy from all of their Pokémon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
