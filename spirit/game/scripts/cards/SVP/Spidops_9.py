from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ba8a446-8eca-50bd-8905-613355f6bdb4',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spidops.Name',
    display_name='Spidops',
    searchable_by=['Spidops', 'Stage 1', 'Spidops'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    family_id=918,
    abilities=[
        Attack(
            title='String Truss',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Jet Headbutt',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
