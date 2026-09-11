from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="dae97bd3-d83c-5e2e-a311-b9fc0176fa74",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name",
    display_name="Decidueye ex",
    searchable_by=["Decidueye ex", "Stage 2", "ex", "Decidueyeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Sniper's Eye",
            game_text="If your opponent has exactly 4 cards in their hand, ignore all Colorless Energy in the costs of attacks used by this Pokémon.",
            passive=standard_passive("If your opponent has exactly 4 cards in their hand, ignore all Colorless Energy in the costs of attacks used by this Pokémon."),
        ),
        Attack(
            title="Crushing Arrow",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
