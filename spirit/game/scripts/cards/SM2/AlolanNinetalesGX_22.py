from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc4c4714-ebb9-50b0-8b44-6caa55bbea8c',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetalesGX.Name',
    display_name='Alolan Ninetales-GX',
    searchable_by=['Alolan Ninetales-GX', 'Stage 1', 'GX', 'AlolanNinetalesGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=22,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Ice Blade',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Blizzard Edge',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Ice Path-GX',
            game_text="Move all damage counters from this Pokémon to your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
