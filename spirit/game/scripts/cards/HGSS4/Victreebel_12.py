from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d64610a-daf7-5eaf-9929-d1cc6632f732',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name',
    display_name='Victreebel',
    searchable_by=['Victreebel', 'Stage 2', 'Victreebel'],
    subtypes=['Stage 2'],
    collector_number=12,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    family_id=69,
    abilities=[
        Ability(
            title='Tangling Tendrils',
            game_text="As long as Victreebel is your Active Pokémon, your opponent's Active Pokémon's Retreat Cost is ColorlessColorless more.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("As long as Victreebel is your Active Pokémon, your opponent's Active Pokémon's Retreat Cost is ColorlessColorless more."),
        ),
        Attack(
            title='Acidic Drain',
            game_text='The Defending Pokémon is now Burned and Poisoned. Remove 3 damage counters from Victreebel.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
