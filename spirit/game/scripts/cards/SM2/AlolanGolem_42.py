from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='03206966-be57-51e2-b229-a5130ecf4455',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name',
    display_name='Alolan Golem',
    searchable_by=['Alolan Golem', 'Stage 2', 'AlolanGolem'],
    subtypes=['Stage 2'],
    collector_number=42,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
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
            title='Electromagnetic Rock Wrecker',
            game_text='Flip a coin for each Lightning Energy attached to this Pokémon. This attack does 80 damage for each heads.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Slam',
            game_text="This attack does 30 less damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
