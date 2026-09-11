from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5740da42-2ffe-5b54-abf5-da3cfd4c5e9d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    display_name='Cosmoem',
    searchable_by=['Cosmoem', 'Stage 1', 'Cosmoem'],
    subtypes=['Stage 1'],
    collector_number=101,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    family_id=789,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, this Pokémon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
