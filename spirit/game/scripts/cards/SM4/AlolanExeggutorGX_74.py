from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7e08373-11ca-5968-9599-142abbac60d2',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorGX.Name',
    display_name='Alolan Exeggutor-GX',
    searchable_by=['Alolan Exeggutor-GX', 'Stage 1', 'GX', 'AlolanExeggutorGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=74,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Attack(
            title='Tropical Head',
            game_text="This attack does 20 damage times the amount of Energy attached to this Pokémon to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Hammer',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Tower-Go-Round-GX',
            game_text="Move any number of Energy from your Pokémon to your other Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
