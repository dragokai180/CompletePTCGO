from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37cb2c86-d943-595e-981f-912e8c2b2b0d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name',
    display_name='Tentacruel',
    searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'],
    subtypes=['Stage 1'],
    collector_number=73,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    family_id=72,
    abilities=[
        Attack(
            title='Poisonous Whip',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Tentacular Panic',
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads. If the first flip is tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
