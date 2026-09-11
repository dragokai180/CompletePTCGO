from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c66198bb-0758-5ea0-88e1-5a44c749b9f6',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name',
    display_name='Aurorus',
    searchable_by=['Aurorus', 'Stage 2', 'Aurorus'],
    subtypes=['Stage 2'],
    collector_number=28,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name',
    family_id=698,
    abilities=[
        Attack(
            title='Frost Wall',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Evolution Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Blizzard Burn',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
