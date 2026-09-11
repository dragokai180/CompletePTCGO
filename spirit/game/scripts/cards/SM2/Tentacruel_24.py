from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2ca106b1-cadf-512b-a5c2-ee22b15f62da',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name',
    display_name='Tentacruel',
    searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    family_id=72,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Seething Tentacles',
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
