from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85b2255d-2d34-56e1-bf99-c27ed9f0e43a',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name',
    display_name='Ampharos',
    searchable_by=['Ampharos', 'Stage 2', 'Ampharos'],
    subtypes=['Stage 2'],
    collector_number=14,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    family_id=179,
    abilities=[
        Attack(
            title='Acceleration Bolt',
            game_text='Search your deck for up to 2 basic Energy cards and attach them to 1 of your Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='Flip a coin. If tails, Ampharos does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
