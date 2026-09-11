from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="43874d7b-094b-5873-a6c3-9516cd7089b1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocksex.Name",
    display_name="Sandy Shocks ex",
    searchable_by=["Sandy Shocks ex", "Basic", "ex", "Ancient", "SandyShocksex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=56,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    abilities=[
        Ability(
            title="Magnetic Absorption",
            game_text="Once during your turn, if your opponent has 4 or fewer Prize cards remaining, you may attach a Basic Fighting Energy card from your discard pile to this Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Earthen Spike",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
