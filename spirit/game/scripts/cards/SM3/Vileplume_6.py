from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d653ecab-8125-525c-95b2-a407c015bc63',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name',
    display_name='Vileplume',
    searchable_by=['Vileplume', 'Stage 2', 'Vileplume'],
    subtypes=['Stage 2'],
    collector_number=6,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Disgusting Pollen',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Basic Pokémon can't attack.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Basic Pokémon can't attack."),
        ),
        Attack(
            title='Downer Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep. If tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
