from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="057ff611-d38f-5d71-8810-0412bc7ff4bc",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1", "Crabominable"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pokémon cost Colorless less for each Kofu card in your discard pile.",
            effect=standard_ability,
        ),
        Attack(
            title="Haymaker",
            game_text="During your next turn, this Pokémon can't use Haymaker.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=250,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
