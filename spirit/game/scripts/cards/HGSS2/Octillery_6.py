from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='23ad3e20-fbaa-5a32-86e0-4c6c781733af',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name',
    display_name='Octillery',
    searchable_by=['Octillery', 'Stage 1', 'Octillery'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    family_id=223,
    abilities=[
        Attack(
            title='Switch Cannon',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Switch Octillery with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ink Bomb',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
