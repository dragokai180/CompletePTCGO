from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='183f0780-c36a-5d81-949e-a786247261c4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name',
    display_name='Dewgong',
    searchable_by=['Dewgong', 'Stage 1', 'Dewgong'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name',
    family_id=86,
    abilities=[
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Dual Blizzard',
            game_text="Discard 2 Energy from this Pokémon. This attack does 60 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
