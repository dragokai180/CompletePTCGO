from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import reversal_trigger

card = PokemonToolCardDef(
    guid="3c862029-3ba2-5d1e-9408-6d02485f6cf2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReversalTrigger.Name",
    display_name="Reversal Trigger",
    searchable_by=["Reversal Trigger", "Pokémon Tool", "Team Plasma"],
    subtypes=["Pokémon Tool", "Team Plasma"],
    collector_number=86,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    granted_abilities=[Ability(
        title="Reversal Trigger",
        game_text="When the Team Plasma Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
        trigger=Triggers.ON_KNOCKED_OUT,
        effect=reversal_trigger,
    )],
)
