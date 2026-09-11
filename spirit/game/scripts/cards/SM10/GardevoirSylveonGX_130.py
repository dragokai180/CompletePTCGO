from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab303b67-067b-5b0f-84f7-129bd0de55ff',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirSylveonGX.Name',
    display_name='Gardevoir & Sylveon-GX',
    searchable_by=['Gardevoir & Sylveon-GX', 'Basic', 'TAG TEAM', 'GX', 'GardevoirSylveonGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=130,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=260,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title='Fairy Song',
            game_text='Search your deck for up to 2 Fairy Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Kaleidostorm',
            game_text='Move any number of Energy from your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Magical Miracle-GX',
            game_text="If this Pokémon has at least 3 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles their hand into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 3},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
