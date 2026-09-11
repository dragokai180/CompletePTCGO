from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15ecb78f-c21f-5bdb-8584-994878895fea',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonBREAK.Name',
    display_name='Hydreigon BREAK',
    searchable_by=['Hydreigon BREAK', 'BREAK', 'HydreigonBREAK'],
    subtypes=['BREAK'],
    collector_number=87,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name',
    family_id=633,
    abilities=[
        Attack(
            title='Calamity Blast',
            game_text="Discard 3 Energy attached to this Pokémon. This attack does 50 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
