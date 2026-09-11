from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2e741fa2-6015-57c7-b249-7b816c90f5a9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakingex.Name",
    display_name="Slaking ex",
    searchable_by=["Slaking ex", "Stage 2", "ex", "Slakingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=147,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Born to Slack",
            game_text="If your opponent has no Pokémon ex or Pokémon V in play, this Pokémon can't attack.",
            passive=standard_passive("If your opponent has no Pokémon ex or Pokémon V in play, this Pokémon can't attack."),
        ),
        Attack(
            title="Great Swing",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=280,
            effect=standard_attack,
        ),
    ],
)
