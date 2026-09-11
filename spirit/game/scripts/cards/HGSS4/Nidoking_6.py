from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2903b0c1-a8c3-5f35-aa63-8223a89b2aec',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name',
    display_name='Nidoking',
    searchable_by=['Nidoking', 'Stage 2', 'Nidoking'],
    subtypes=['Stage 2'],
    collector_number=6,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    family_id=32,
    abilities=[
        Ability(
            title='Pheromone Stamina',
            game_text='Nidoking gets +20 HP for each Nidoqueen you have in play.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Nidoking gets +20 HP for each Nidoqueen you have in play.'),
        ),
        Attack(
            title='Venomous Horn',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
