from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9b3105ef-d2c0-5b91-bd44-861eb1f9bae3',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name',
    display_name='Infernape',
    searchable_by=['Infernape', 'Stage 2', 'Infernape'],
    subtypes=['Stage 2'],
    collector_number=59,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name',
    family_id=392,
    abilities=[
        Ability(
            title='Flaming Fighter',
            game_text="Put 6 damage counters instead of 2 on your opponent's Burned Pokémon between turns.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Burst Punch',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
