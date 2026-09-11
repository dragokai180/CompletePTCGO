from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5baa0a77-707b-5cd2-a34b-b4083084936f',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name',
    display_name='Golem',
    searchable_by=['Golem', 'Stage 2', 'Golem'],
    subtypes=['Stage 2'],
    collector_number=89,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Steamroller',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Slam',
            game_text="This attack does 20 less damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
