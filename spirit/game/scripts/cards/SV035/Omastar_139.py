from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9e17862-fda1-5435-ad63-30ac4b63f79e',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name',
    display_name='Omastar',
    searchable_by=['Omastar', 'Stage 2', 'Omastar'],
    subtypes=['Stage 2'],
    collector_number=139,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    family_id=138,
    abilities=[
        Ability(
            title='Primordial Tentacles',
            game_text="As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon can't retreat.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon can't retreat."),
        ),
        Attack(
            title='Aqua Split',
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
