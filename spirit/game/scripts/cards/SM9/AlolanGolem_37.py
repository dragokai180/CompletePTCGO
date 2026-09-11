from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='14d44cd7-52c2-5dee-ae52-20dcae095fba',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name',
    display_name='Alolan Golem',
    searchable_by=['Alolan Golem', 'Stage 2', 'AlolanGolem'],
    subtypes=['Stage 2'],
    collector_number=37,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Electromagnetic Bomb',
            game_text='Move any number of Lightning Energy from your Benched Pokémon to this Pokémon. This attack does 20 damage for each Energy card you moved in this way.',
            cost={},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Super Zap Cannon',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 4},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
